import cadquery as cq
w0=cq.Workplane('YZ',origin=(-96,0,0))
w1=cq.Workplane('XY',origin=(0,0,-17))
r=w0.workplane(offset=102/2).moveTo(-95.5,3.5).box(9,73,102).union(w0.sketch().arc((1,73),(-24,-51),(100,-24)).segment((58,-24)).segment((58,49)).arc((23,45),(1,73)).assemble().finalize().extrude(137)).union(w1.workplane(offset=51/2).moveTo(59,4).cylinder(51,37))