
"use strict";

let ParamGet = require('./ParamGet.js')
let StreamRate = require('./StreamRate.js')
let SetMode = require('./SetMode.js')
let MessageInterval = require('./MessageInterval.js')
let CommandTOL = require('./CommandTOL.js')
let FileMakeDir = require('./FileMakeDir.js')
let CommandTriggerControl = require('./CommandTriggerControl.js')
let WaypointPull = require('./WaypointPull.js')
let CommandAck = require('./CommandAck.js')
let CommandLong = require('./CommandLong.js')
let FileRename = require('./FileRename.js')
let ParamPush = require('./ParamPush.js')
let FileWrite = require('./FileWrite.js')
let FileTruncate = require('./FileTruncate.js')
let LogRequestData = require('./LogRequestData.js')
let WaypointPush = require('./WaypointPush.js')
let FileClose = require('./FileClose.js')
let FileRemoveDir = require('./FileRemoveDir.js')
let LogRequestEnd = require('./LogRequestEnd.js')
let FileList = require('./FileList.js')
let CommandHome = require('./CommandHome.js')
let CommandVtolTransition = require('./CommandVtolTransition.js')
let ParamSet = require('./ParamSet.js')
let FileChecksum = require('./FileChecksum.js')
let CommandInt = require('./CommandInt.js')
let WaypointSetCurrent = require('./WaypointSetCurrent.js')
let SetMavFrame = require('./SetMavFrame.js')
let FileRemove = require('./FileRemove.js')
let ParamPull = require('./ParamPull.js')
let CommandTriggerInterval = require('./CommandTriggerInterval.js')
let MountConfigure = require('./MountConfigure.js')
let FileRead = require('./FileRead.js')
let LogRequestList = require('./LogRequestList.js')
let WaypointClear = require('./WaypointClear.js')
let CommandBool = require('./CommandBool.js')
let VehicleInfoGet = require('./VehicleInfoGet.js')
let FileOpen = require('./FileOpen.js')

module.exports = {
  ParamGet: ParamGet,
  StreamRate: StreamRate,
  SetMode: SetMode,
  MessageInterval: MessageInterval,
  CommandTOL: CommandTOL,
  FileMakeDir: FileMakeDir,
  CommandTriggerControl: CommandTriggerControl,
  WaypointPull: WaypointPull,
  CommandAck: CommandAck,
  CommandLong: CommandLong,
  FileRename: FileRename,
  ParamPush: ParamPush,
  FileWrite: FileWrite,
  FileTruncate: FileTruncate,
  LogRequestData: LogRequestData,
  WaypointPush: WaypointPush,
  FileClose: FileClose,
  FileRemoveDir: FileRemoveDir,
  LogRequestEnd: LogRequestEnd,
  FileList: FileList,
  CommandHome: CommandHome,
  CommandVtolTransition: CommandVtolTransition,
  ParamSet: ParamSet,
  FileChecksum: FileChecksum,
  CommandInt: CommandInt,
  WaypointSetCurrent: WaypointSetCurrent,
  SetMavFrame: SetMavFrame,
  FileRemove: FileRemove,
  ParamPull: ParamPull,
  CommandTriggerInterval: CommandTriggerInterval,
  MountConfigure: MountConfigure,
  FileRead: FileRead,
  LogRequestList: LogRequestList,
  WaypointClear: WaypointClear,
  CommandBool: CommandBool,
  VehicleInfoGet: VehicleInfoGet,
  FileOpen: FileOpen,
};
