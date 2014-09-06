#!/usr/bin/env python
#
# Super duper small script using inotify to find closed files and delete them
# once they're closed. Useful for instantly removing files uploaded to an ftp
# server (for speedtest purposes) as to not fill up the file system.
#
#
# Copyright (c) 2014 Kristian Larsson <kristian@spritelink.net>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# 

import os
import pyinotify

WATCH_DIR='/srv/ftp/upload'

# The watch manager stores the watches and provides operations on watches
wm = pyinotify.WatchManager()

mask = pyinotify.IN_CLOSE_WRITE | pyinotify.IN_CLOSE_NOWRITE # watched events

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CLOSE(self, event):
        # remove that file, haha!
        os.remove(event.pathname)

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch(WATCH_DIR, mask)
notifier.loop()
