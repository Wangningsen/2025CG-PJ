import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-38))
r=w0.sketch().segment((-99,-36),(-79,-36)).arc((-20,-81),(49,-52)).arc((47,-63),(44,-74)).segment((44,-93)).segment((99,-93)).segment((99,-27)).segment((59,-27)).arc((58,13),(27,51)).segment((27,93)).segment((-99,93)).close().assemble().finalize().extrude(-62).union(w0.workplane(offset=138/2).moveTo(-17,-13).cylinder(138,31))