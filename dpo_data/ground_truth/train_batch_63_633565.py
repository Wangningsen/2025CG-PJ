import cadquery as cq
w0=cq.Workplane('YZ',origin=(-61,0,0))
r=w0.sketch().arc((-23,9),(-87,-77),(8,-28)).segment((100,-28)).segment((100,96)).segment((-23,96)).close().assemble().reset().face(w0.sketch().segment((-18,23),(31,-23)).segment((95,45)).segment((45,91)).close().assemble(),mode='s').finalize().extrude(123)