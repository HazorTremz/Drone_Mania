# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/hazortremz/my_drone_space/src/mavlink

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/hazortremz/my_drone_space/build/mavlink

# Utility rule file for ardupilotmega.xml-v1.0.

# Include the progress variables for this target.
include CMakeFiles/ardupilotmega.xml-v1.0.dir/progress.make

CMakeFiles/ardupilotmega.xml-v1.0: include/v1.0/ardupilotmega/ardupilotmega.h


include/v1.0/ardupilotmega/ardupilotmega.h: /home/hazortremz/my_drone_space/src/mavlink/message_definitions/v1.0/ardupilotmega.xml
include/v1.0/ardupilotmega/ardupilotmega.h: /home/hazortremz/my_drone_space/src/mavlink/message_definitions/v1.0/common.xml
include/v1.0/ardupilotmega/ardupilotmega.h: /home/hazortremz/my_drone_space/src/mavlink/pymavlink/tools/mavgen.py
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/hazortremz/my_drone_space/build/mavlink/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating include/v1.0/ardupilotmega/ardupilotmega.h"
	/usr/bin/env PYTHONPATH="/home/hazortremz/my_drone_space/src/mavlink:/opt/ros/noetic/lib/python3/dist-packages" /usr/bin/python3.8 /home/hazortremz/my_drone_space/src/mavlink/pymavlink/tools/mavgen.py --lang=C --wire-protocol=1.0 --output=include/v1.0 /home/hazortremz/my_drone_space/src/mavlink/message_definitions/v1.0/ardupilotmega.xml

ardupilotmega.xml-v1.0: CMakeFiles/ardupilotmega.xml-v1.0
ardupilotmega.xml-v1.0: include/v1.0/ardupilotmega/ardupilotmega.h
ardupilotmega.xml-v1.0: CMakeFiles/ardupilotmega.xml-v1.0.dir/build.make

.PHONY : ardupilotmega.xml-v1.0

# Rule to build all files generated by this target.
CMakeFiles/ardupilotmega.xml-v1.0.dir/build: ardupilotmega.xml-v1.0

.PHONY : CMakeFiles/ardupilotmega.xml-v1.0.dir/build

CMakeFiles/ardupilotmega.xml-v1.0.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/ardupilotmega.xml-v1.0.dir/cmake_clean.cmake
.PHONY : CMakeFiles/ardupilotmega.xml-v1.0.dir/clean

CMakeFiles/ardupilotmega.xml-v1.0.dir/depend:
	cd /home/hazortremz/my_drone_space/build/mavlink && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/hazortremz/my_drone_space/src/mavlink /home/hazortremz/my_drone_space/src/mavlink /home/hazortremz/my_drone_space/build/mavlink /home/hazortremz/my_drone_space/build/mavlink /home/hazortremz/my_drone_space/build/mavlink/CMakeFiles/ardupilotmega.xml-v1.0.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/ardupilotmega.xml-v1.0.dir/depend

