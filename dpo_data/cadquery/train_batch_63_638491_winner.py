import cadquery as cq
w0=cq.Workplane('YZ',origin=(27,0,0))
r=w0.sketch().push([(0,58)]).circle(42).push([(5,39.5)]).rect(28,39,mode='s').finalize().extrude(-80).union(w0.sketch().push([(12,-23)]).circle(30).push([(-6.5,-80)]).rect(13,40).finalize().extrude(26))