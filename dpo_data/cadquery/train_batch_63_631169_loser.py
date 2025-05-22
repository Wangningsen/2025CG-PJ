import cadquery as cq
w0=cq.Workplane('YZ',origin=(-63,0,0))
w1=cq.Workplane('XY',origin=(0,0,-6))
r=w0.sketch().arc((70,-34),(75,-32),(80,-34)).segment((80,-24)).segment((70,-24)).close().assemble().finalize().extrude(163).union(w1.workplane(offset=40/2).moveTo(-23,-3).cylinder(40,77))