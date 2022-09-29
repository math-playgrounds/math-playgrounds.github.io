#!/usr/bin/env bash
##
# Copy mathplayground's svelte app into django
#

DEST_DIR="media/mathplayground/"
ORIG_DIR="$HOME/public_html/mathplayground/public/"

cp -r $ORIG_DIR/* $DEST_DIR/
