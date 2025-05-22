import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,71))
w1=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.workplane(offset=-143/2).moveTo(35,0).cylinder(143,65).union(w0.sketch().segment((-29,-55),(99,-55)).segment((99,55)).segment((-29,55)).segment((-29,3)).segment((-20,3)).segment((-20,-36)).segment((-29,-36)).close().assemble().finalize().extrude(-45)).union(w1.sketch().segment((-44,26),(-36,26)).segment((-36,71)).arc((-40,69),(-44,71)).close().assemble().finalize().extrude(130))