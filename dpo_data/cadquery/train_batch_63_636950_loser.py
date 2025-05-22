import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-69))
r=w0.sketch().segment((-94,56),(-61,1)).segment((9,43)).arc((86,2),(14,54)).segment((-17,100)).close().assemble().finalize().extrude(55).union(w0.sketch().segment((33,-99),(41,-100)).segment((45,-71)).arc((51,-71),(57,-69)).arc((59,-68),(61,-68)).arc((55,2),(36,-69)).close().assemble().finalize().extrude(138))