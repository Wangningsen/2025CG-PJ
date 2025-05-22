import cadquery as cq
w0=cq.Workplane('YZ',origin=(-50,0,0))
r=w0.sketch().arc((75,-66),(77,-61),(82,-57)).arc((-80,60),(75,-66)).assemble().finalize().extrude(100)