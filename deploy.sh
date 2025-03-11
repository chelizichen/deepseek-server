#!/usr/bin/env bash
# Written in [Amber](https://amber-lang.com/)
# version: 0.3.5-alpha
# date: 2025-03-11 15:57:26


exit__80_v0() {
    local code=$1
    exit "${code}";
    __AS=$?
}
__0_server_name="DeepSeekBackServer"
remove_old__94_v0() {
    rm -r build;
    __AS=$?;
if [ $__AS != 0 ]; then
        echo "[ignore] remove build failed"
fi
    rm -r dist;
    __AS=$?;
if [ $__AS != 0 ]; then
        echo "[ignore] remove dist failed"
fi
}
build__95_v0() {
    pyinstaller main.spec --clean;
    __AS=$?;
if [ $__AS != 0 ]; then
        echo "build failed"
        exit__80_v0 1;
        __AF_exit80_v0__16_9="$__AF_exit80_v0";
        echo "$__AF_exit80_v0__16_9" > /dev/null 2>&1
fi
    cp ./sgrid.yml ./dist/sgrid.yml;
    __AS=$?;
if [ $__AS != 0 ]; then
        echo "copy sgrid.yml failed"
fi
}
release__96_v0() {
    cd ./dist;
    __AS=$?;
if [ $__AS != 0 ]; then
        echo "cd failed"
        exit__80_v0 1;
        __AF_exit80_v0__26_9="$__AF_exit80_v0";
        echo "$__AF_exit80_v0__26_9" > /dev/null 2>&1
fi
    tar -zcvf "${__0_server_name}".tar.gz ./*;
    __AS=$?;
if [ $__AS != 0 ]; then
        echo "tar failed"
        exit__80_v0 1;
        __AF_exit80_v0__30_9="$__AF_exit80_v0";
        echo "$__AF_exit80_v0__30_9" > /dev/null 2>&1
fi
    mv ./"${__0_server_name}".tar.gz ../;
    __AS=$?;
if [ $__AS != 0 ]; then
        echo "mv failed"
        exit__80_v0 1;
        __AF_exit80_v0__34_9="$__AF_exit80_v0";
        echo "$__AF_exit80_v0__34_9" > /dev/null 2>&1
fi
    cd ../;
    __AS=$?;
if [ $__AS != 0 ]; then
        echo "cd failed"
        exit__80_v0 1;
        __AF_exit80_v0__38_9="$__AF_exit80_v0";
        echo "$__AF_exit80_v0__38_9" > /dev/null 2>&1
fi
}
args=("$0" "$@")
    remove_old__94_v0 ;
    __AF_remove_old94_v0__43_5="$__AF_remove_old94_v0";
    echo "$__AF_remove_old94_v0__43_5" > /dev/null 2>&1
    build__95_v0 ;
    __AF_build95_v0__44_5="$__AF_build95_v0";
    echo "$__AF_build95_v0__44_5" > /dev/null 2>&1
    release__96_v0 ;
    __AF_release96_v0__45_5="$__AF_release96_v0";
    echo "$__AF_release96_v0__45_5" > /dev/null 2>&1
