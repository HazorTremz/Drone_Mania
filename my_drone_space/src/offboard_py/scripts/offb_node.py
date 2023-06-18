#! /usr/bin/env python3
import rospy

from sensor_msgs.msg import TimeReference  
from geometry_msgs.msg import PoseStamped,TwistStamped
from mavros_msgs.msg import State, Thrust
from mavros_msgs.srv import CommandBool, CommandBoolRequest, SetMode, SetModeRequest, ParamPush,ParamPushRequest
from mavros_msgs.srv import ParamGet, ParamGetRequest, ParamGetResponse

current_state = State()
current_orien = PoseStamped()
time_stamp = TimeReference
flag_1 = False
flag_2 = False
flag_3 = False
flag_4 = False
flag_5 = False
flag_6 = False
flag_7 = False
flag_8 = False
flag_9 = False
reached = False
land = False
up_down1 = False
up_down2 = False
up_down3 = False

def state_cb(msg):
    global current_state
    current_state = msg

def orien_cb(msg):
    global current_orien
    current_orien=  msg
def time_cb(msg):
    global time_stamp
    time_stamp = msg
if __name__ == "__main__":
    rospy.init_node("offb_node_py")

    state_sub = rospy.Subscriber("mavros/state", State, callback = state_cb)
    #time_sub = rospy.Subscriber("mavros/time_reference",TimeReference, callback=time_cb)
    orientation_sub = rospy.Subscriber("mavros/local_position/pose",PoseStamped, callback= orien_cb )
    local_pos_pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped, queue_size=10)
    local_vel_pub = rospy.Publisher("/mavros/setpoint_velocity/cmd_vel", TwistStamped, queue_size=10)
    #setpoint_pub = rospy.Publisher('/mavros/setpoint_attitude/thrust', Thrust, queue_size=10)

    rospy.wait_for_service("/mavros/cmd/arming")
    arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)    

    rospy.wait_for_service("/mavros/set_mode")
    set_mode_client = rospy.ServiceProxy("mavros/set_mode", SetMode)
    # set_param_client = rospy.ServiceProxy("mavros/param/push", ParamPush)
    # param_get = rospy.ServiceProxy('/mavros/param/get', ParamGet)
    # Setpoint publishing MUST be faster than 2Hz
    rate = rospy.Rate(20)
    # Wait for Flight Controller connection
    while(not rospy.is_shutdown() and not current_state.connected):
        rate.sleep()
        # pose = PoseStamped()
        vel_msg = TwistStamped()
        vel_msg.header.frame_id = "base_link"
        vel_msg.twist.linear.x = 0.0 # set desired x velocity here
        vel_msg.twist.linear.y = 0.0 # set desired y velocity here
        vel_msg.twist.linear.z = 5.0 # set desired z velocity here
        vel_msg.twist.angular.x = 0.0
        vel_msg.twist.angular.y = 0.0
        vel_msg.twist.angular.z = 0.0

        # Send a few setpoints before starting
        for i in range(100):   
            if(rospy.is_shutdown()):
                break
            vel_msg.header.stamp = rospy.Time.now()
            local_vel_pub.publish(vel_msg)
            # local_pos_pub.publish(pose)
            rate.sleep()
        offb_set_mode = SetModeRequest()
        offb_set_mode.custom_mode = 'OFFBOARD'
 
        arm_cmd = CommandBoolRequest()
        arm_cmd.value = True

        last_req = rospy.Time.now()
    while(not rospy.is_shutdown()):
        
        if (reached == False):
            vel_msg.header.stamp = rospy.Time.now()
            local_vel_pub.publish(vel_msg)
        # if (land == True):
        #     offb_set_mode.custom_mode = "AUTO.LAND"
        # setpoint_pub.publish(thrust_msg)
        #vel.header.stamp = time_stamp.header.stamp
        if(current_state.mode != "OFFBOARD" and (rospy.Time.now() - last_req) > rospy.Duration(5.0)):
            if(set_mode_client.call(offb_set_mode).mode_sent == True):
                rospy.loginfo("OFFBOARD enabled")
            
            last_req = rospy.Time.now()
        else:
            if(not current_state.armed and (rospy.Time.now() - last_req) > rospy.Duration(5.0)):
                if(arming_client.call(arm_cmd).success == True):
                    rospy.loginfo("Vehicle armed")
            
                last_req = rospy.Time.now()
       
        x_val = current_orien.pose.position.x
        y_val = current_orien.pose.position.y
        z_val = current_orien.pose.position.z
        rospy.loginfo(x_val)
        rospy.loginfo(y_val)
        rospy.loginfo(z_val)
        yaw = current_orien.pose.orientation.w
        if (z_val > 1 and flag_1==False):
            vel_msg.twist.linear.y = -2.0
            vel_msg.twist.linear.z = 0.0
            flag_1 = True
        if(y_val < -7 and flag_2==False):
            vel_msg.twist.linear.y = 0.0
            vel_msg.twist.linear.x = 2.0
            flag_2 = True
        if( x_val > 5 and flag_3==False):
            vel_msg.twist.linear.x = 0.0
            vel_msg.twist.linear.z = 0.0
            vel_msg.twist.linear.y = -2.0
            flag_3 = True
        if(y_val <  4 and x_val < -6 and flag_4==False):
            vel_msg.twist.linear.x = -2.0
            vel_msg.twist.linear.y = 0.0
            flag_4 = True
        if(x_val < -11.5 and flag_5==False):
            vel_msg.twist.linear.x = 0.0
            vel_msg.twist.linear.z = 0.0
            vel_msg.twist.linear.y = 2.0
            flag_5 = True
        if(x_val < -11.5 and y_val > 19.5 and flag_6==False):
            vel_msg.twist.linear.x = 0.0
            vel_msg.twist.linear.y = 0.0
            flag_6 = True
        if (flag_6 == True):
            if (z_val < 14 and reached == False):
                vel_msg.twist.linear.z = 2.0
            else :  
                reached = True 
                if (land == False):
                    pose = PoseStamped()
                    pose.pose.position.x = 0
                    pose.pose.position.y = 0
                    pose.pose.position.z = 0
                    if ((x_val != 0) and (y_val != 0) and (z_val != 0)):
                        local_pos_pub.publish(pose)
                    else: 
                        land = True
                while (current_state.mode == "OFFBOARD" and land == True):
                    offb_set_mode.custom_mode = "AUTO.LAND"
                    rate.sleep()
        rate.sleep()
