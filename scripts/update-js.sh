#!/usr/bin/env bash
##
# Copy mathplayground's svelte app into django
#

DEST_DIR="media/mathplayground/"
ORIG_DIR="$HOME/public_html/mathplayground/public/"

rm -rf $DEST_DIR
mkdir $DEST_DIR
cp -r $ORIG_DIR/* $DEST_DIR
