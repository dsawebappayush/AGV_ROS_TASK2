#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/pc/catkin_ws/src/turtlebot4/turtlebot3_teleop"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/pc/catkin_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/pc/catkin_ws/install/lib/python3/dist-packages:/home/pc/catkin_ws/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/pc/catkin_ws/build" \
    "/usr/bin/python3" \
    "/home/pc/catkin_ws/src/turtlebot4/turtlebot3_teleop/setup.py" \
     \
    build --build-base "/home/pc/catkin_ws/build/turtlebot4/turtlebot3_teleop" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/pc/catkin_ws/install" --install-scripts="/home/pc/catkin_ws/install/bin"
