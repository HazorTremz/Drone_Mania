#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State, AttitudeTarget
from mavros_msgs.srv import CommandBool, CommandBoolRequest, SetMode, SetModeRequest
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import TimeReference, Image, Joy
current_state = State()
current_orien = PoseStamped()
object_detected = False
flag_inititate = True
joy_val = Joy()
start = False
def state_cb(msg):
    global current_state
    current_state = msg
def joy_cb(msg):
    global joy_val
    joy_val = msg
def img_cb(msg):
    global obj_distance
    bridge = CvBridge()
    try:
      cv_image = bridge.imgmsg_to_cv2(msg,desired_encoding='32FC1')
    except CvBridgeError as e:
      print(e)
    obj_distance = cv_image[cv_image.shape[0]//2, cv_image.shape[1]//2]
    # cv2.imwrite(cv_image)
    # cv2.imshow("image",cv_image)
    # cv2.waitKey(3)
def orien_cb(msg):
    global current_orien
    current_orien=  msg
if __name__ == "__main__":
    rospy.init_node("offb_node_py")
    image_sub = rospy.Subscriber("/iris/camera/depth/image_raw", Image,callback=img_cb)
    state_sub = rospy.Subscriber("mavros/state", State, callback = state_cb)
    orientation_sub = rospy.Subscriber("mavros/local_position/pose",PoseStamped, callback= orien_cb )
    local_pos_pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped, queue_size=10)
    joy_sub = rospy.Subscriber("/joy",Joy, callback= joy_cb )
    rospy.wait_for_service("/mavros/cmd/arming")
    arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)    

    rospy.wait_for_service("/mavros/set_mode")
    set_mode_client = rospy.ServiceProxy("mavros/set_mode", SetMode)
    

    # Setpoint publishing MUST be faster than 2Hz
    rate = rospy.Rate(20)

    # Wait for Flight Controller connection
    while(not rospy.is_shutdown() and not current_state.connected):
        rate.sleep()
    # Send a few setpoints before starting
    for i in range(100):   
        if(rospy.is_shutdown()):
            break
        rate.sleep()

    offb_set_mode = SetModeRequest()
    offb_set_mode.custom_mode = 'POSCTL'

    arm_cmd = CommandBoolRequest()
    arm_cmd.value = True

    last_req = rospy.Time.now()

    while(not rospy.is_shutdown()):
        if(obj_distance < 2.5 or object_detected == True):
            object_detected = True
            # rospy.loginfo(current_orien)
            if (flag_inititate == True):
                stay_x = current_orien.pose.position.x
                stay_y = current_orien.pose.position.y
                stay_z = current_orien.pose.position.z
                stay_x_ang = current_orien.pose.orientation.x                
                stay_y_ang = current_orien.pose.orientation.y
                stay_z_ang = current_orien.pose.orientation.z
                stay_w_ang = current_orien.pose.orientation.w
                flag_inititate = False
            else:
                if (joy_val.axes[4] > 0.0):
                    rospy.loginfo(joy_val.axes)
                    offb_set_mode.custom_mode = "OFFBOARD"
                    if current_state.mode != "OFFBOARD":
                        if (set_mode_client.call(offb_set_mode).mode_sent == True):
                            rospy.loginfo("OFFBOARD mode enabled")
                    pose1 = PoseStamped()
                    pose1.pose.position.x = stay_x
                    pose1.pose.position.y = stay_y
                    pose1.pose.position.z = stay_z
                    pose1.pose.orientation.x = stay_x_ang
                    pose1.pose.orientation.y = stay_y_ang
                    pose1.pose.orientation.z = stay_z_ang
                    pose1.pose.orientation.w = stay_w_ang
                    local_pos_pub.publish(pose1)
                    rospy.loginfo("collision detected")
                else:
                    object_detected = False
                    flag_inititate = True
                    offb_set_mode.custom_mode = "POSCTL"
                    if current_state.mode != "POSCTL":
                        if (set_mode_client.call(offb_set_mode).mode_sent == True):
                            rospy.loginfo("POSCTL mode enabled")

        if (start == False):  
            if(current_state.mode != "POSCTL" and (rospy.Time.now() - last_req) > rospy.Duration(5.0)):
                if(set_mode_client.call(offb_set_mode).mode_sent == True):
                    rospy.loginfo("POSCTL enabled")
                
                last_req = rospy.Time.now()
            else:
                if(not current_state.armed and (rospy.Time.now() - last_req) > rospy.Duration(5.0)):
                    if(arming_client.call(arm_cmd).success == True):
                        rospy.loginfo("Vehicle armed")
                        start == True               
                    last_req = rospy.Time.now()
        rate.sleep()