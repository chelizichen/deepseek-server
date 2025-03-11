#!/usr/bin/env bash
# Written in [Amber](https://amber-lang.com/)
# version: 0.3.5-alpha
# date: 2025-03-11 15:50:25
build__0_v0() {
     npm run build ;
    __AS=$?;
if [ $__AS != 0 ]; then
        echo "build failed"
fi
}
release__1_v0() {
     npm run release ;
    __AS=$?;
if [ $__AS != 0 ]; then
        echo "release failed"
fi
}
args=("$0" "$@")
    build__0_v0 ;
    __AF_build0_v0__14_9="$__AF_build0_v0";
    echo "$__AF_build0_v0__14_9" > /dev/null 2>&1
    release__1_v0 ;
    __AF_release1_v0__15_9="$__AF_release1_v0";
    echo "$__AF_release1_v0__15_9" > /dev/null 2>&1
