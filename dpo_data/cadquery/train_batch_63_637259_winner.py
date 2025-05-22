import cadquery as cq
w0=cq.Workplane('YZ',origin=(33,0,0))
r=w0.sketch().segment((-99,-10),(-69,29)).segment((-7,-16)).segment((-53,-80)).arc((81,-55),(65,80)).arc((10,14),(-41,96)).arc((-87,54),(-99,-10)).assemble().finalize().extrude(-67)