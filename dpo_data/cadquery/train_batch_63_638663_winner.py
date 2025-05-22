import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().arc((-20,-3),(-70,-49),(-10,-76)).segment((71,-76)).segment((71,82)).segment((-20,82)).close().assemble().finalize().extrude(-200)