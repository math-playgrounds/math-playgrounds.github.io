#!/usr/bin/env bash
##
# Set up symlinks for mathplayground development
#

DEST_DIR="media/mathplayground/"
ORIG_DIR="$HOME/public_html/mathplayground/public/"

rm -rf $DEST_DIR

ln -s $ORIG_DIR $DEST_DIR
