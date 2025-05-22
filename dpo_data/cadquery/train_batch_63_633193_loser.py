import cadquery as cq
w0=cq.Workplane('YZ',origin=(74,0,0))
r=w0.sketch().segment((-100,49),(-85,40)).arc((-91,-26),(-35,-74)).segment((-35,-96)).segment((-6,-96)).segment((-6,-74)).arc((25,-60),(48,-37)).arc((96,43),(8,71)).arc((2,73),(-6,74)).segment((-6,96)).segment((-35,96)).segment((-35,74)).arc((-62,63),(-81,46)).segment((-96,61)).close().assemble().finalize().extrude(-148)