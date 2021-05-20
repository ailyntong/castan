#!/bin/bash

pushd $HOME >> /dev/null
if [ ! -f moon-gen/.built ]; then
    git clone --depth=1 git://github.com/emmericp/MoonGen.git moon-gen

    cd moon-gen
    # ./build.sh
    git submodule update --init
    cd libmoon
    git submodule update --init --recursive
    patch ~/moon-gen/libmoon/deps/dpdk/mk/rte.vars.mk < ~/castan/experiments/libmoon_rte.vars.mk.patch
    ./build.sh --moongen

    touch .built
fi

popd >> /dev/null
