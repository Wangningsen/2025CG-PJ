import cadquery as cq
w0=cq.Workplane('YZ',origin=(16,0,0))
r=w0.sketch().push([(-89.5,-54)]).rect(21,72).push([(-93,-28)]).circle(6,mode='s').finalize().extrude(-32).union(w0.sketch().arc((39,80),(-15,29),(60,29)).arc((98,69),(41,81)).arc((40,81),(39,80)).assemble().finalize().extrude(-4))