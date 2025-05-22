import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().arc((-75,47),(-21,-42),(76,-6)).segment((19,-24)).segment((19,-27)).segment((11,-27)).segment((11,-21)).segment((6,-22)).segment((6,-16)).segment((-6,-8)).segment((-6,-7)).close().assemble().finalize().extrude(-200)