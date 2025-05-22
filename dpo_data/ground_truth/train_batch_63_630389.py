import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-79))
r=w0.sketch().segment((-92,-55),(28,-100)).segment((45,-54)).segment((-18,-28)).arc((-48,-59),(-86,-40)).close().assemble().finalize().extrude(150).union(w0.sketch().segment((-77,42),(-23,-73)).segment((78,-25)).segment((51,32)).arc((67,44),(73,64)).arc((-51,-67),(25,97)).arc((15,91),(8,82)).close().assemble().finalize().extrude(158))