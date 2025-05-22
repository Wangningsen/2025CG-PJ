import cadquery as cq
w0=cq.Workplane('YZ',origin=(65,0,0))
r=w0.sketch().segment((-100,47),(-76,-45)).segment((-24,-31)).arc((11,-66),(61,-65)).arc((70,-62),(77,-56)).arc((86,34),(-3,46)).segment((-9,71)).close().assemble().finalize().extrude(-131)