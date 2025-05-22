import cadquery as cq
w0=cq.Workplane('YZ',origin=(34,0,0))
r=w0.sketch().segment((-99,-9),(-70,30)).segment((-7,-16)).segment((-53,-80)).arc((80,-55),(65,80)).arc((2,15),(-41,96)).arc((-88,53),(-99,-9)).assemble().finalize().extrude(-67)