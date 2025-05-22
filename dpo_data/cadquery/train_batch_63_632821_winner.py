import cadquery as cq
w0=cq.Workplane('YZ',origin=(-56,0,0))
w1=cq.Workplane('YZ',origin=(-57,0,0))
r=w0.sketch().arc((-33,-6),(-100,-39),(-32,-74)).arc((-10,-66),(4,-44)).arc((23,-48),(41,-42)).segment((41,-36)).segment((46,-36)).arc((56,-29),(65,-24)).arc((76,-16),(84,-5)).segment((84,-10)).segment((100,-10)).segment((100,26)).segment((92,26)).arc((17,80),(-17,-7)).arc((-25,-4),(-33,-6)).assemble().finalize().extrude(112).union(w1.workplane(offset=98/2).moveTo(33,21).cylinder(98,51))