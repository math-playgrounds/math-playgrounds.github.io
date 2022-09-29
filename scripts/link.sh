#!/usr/bin/env bash
##
# Set up symlinks for mathplayground development
#

DEST_DIR="media/mathplayground/"
ORIG_DIR="$HOME/public_html/mathplayground/public/"

rm -rf $DEST_DIR/build/bundle.js
rm -rf $DEST_DIR/build/bundle.css

ln -s $ORIG_DIR/build/bundle.js $DEST_DIR/build/bundle.js
ln -s $ORIG_DIR/build/bundle.css $DEST_DIR/build/bundle.css
