import cadquery as cq
w0=cq.Workplane('YZ',origin=(-34,0,0))
r=w0.sketch().push([(85.5,47.5)]).rect(17,105).push([(85,48)]).circle(6,mode='s').push([(84,-91)]).circle(9).finalize().extrude(-28).union(w0.sketch().push([(-61,27.5)]).rect(66,137).push([(-53.5,56.5)]).rect(51,29,mode='s').finalize().extrude(96))