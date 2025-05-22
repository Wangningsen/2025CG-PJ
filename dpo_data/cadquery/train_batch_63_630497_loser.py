import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-53))
w1=cq.Workplane('XY',origin=(0,0,-54))
r=w0.sketch().segment((-95,-37),(-8,-37)).segment((-8,-81)).segment((42,-81)).arc((67,-100),(90,-81)).segment((95,-81)).segment((95,33)).segment((81,33)).arc((20,100),(-41,35)).segment((-95,35)).close().assemble().finalize().extrude(107).union(w1.sketch().arc((-64,-30),(-56,-32),(-48,-30)).close().assemble().finalize().extrude(37))