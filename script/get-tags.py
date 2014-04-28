#!/usr/bin/env python

from midonetclient.api import MidonetApi
import sys

def main():
    mn_uri = 'http://localhost:8081'
    my_laptop = 'c1b9eb8a-c83b-43d3-b7b8-8613f921dbe7'
    mc = MidonetApi(mn_uri, 'admin', 'password')

    bridges = mc.get_bridges({'tenant_id': my_laptop})
    for bridge in bridges:
      print("Bridge %s" % bridge.get_id())
      tags = bridge.get_tags()
      for tag in tags:
        print("tag: %s" % tag.get_tag())

if __name__ == '__main__':
    main()
