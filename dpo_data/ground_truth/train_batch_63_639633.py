import cadquery as cq
w0=cq.Workplane('YZ',origin=(72,0,0))
w1=cq.Workplane('XY',origin=(0,0,-42))
r=w0.sketch().segment((-100,86),(-96,48)).segment((-12,57)).segment((-16,95)).close().assemble().finalize().extrude(-17).union(w0.sketch().push([(68,-56)]).rect(64,78).reset().face(w0.sketch().segment((61,-92),(75,-92)).segment((75,-75)).arc((89,-56),(75,-37)).segment((75,-20)).segment((61,-20)).segment((61,-37)).arc((48,-56),(61,-75)).close().assemble(),mode='s').finalize().extrude(21)).union(w1.workplane(offset=100/2).moveTo(-40,32.5).box(106,61,100))