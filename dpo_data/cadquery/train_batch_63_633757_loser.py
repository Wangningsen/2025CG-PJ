import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-94,0))
r=w0.sketch().segment((-100,-39),(-56,-43)).arc((-5,-89),(54,-53)).segment((97,-57)).segment((100,-27)).segment((56,-23)).arc((5,23),(-54,-13)).segment((-97,-9)).close().assemble().finalize().extrude(50).union(w0.sketch().arc((-65,69),(-41,73),(-17,63)).segment((-17,89)).segment((-65,89)).close().assemble().finalize().extrude(188))