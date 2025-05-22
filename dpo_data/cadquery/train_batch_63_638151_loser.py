import cadquery as cq
w0=cq.Workplane('YZ',origin=(-84,0,0))
r=w0.sketch().push([(49,-48.5)]).rect(28,103).push([(36,-28)]).circle(1,mode='s').finalize().extrude(158).union(w0.workplane(offset=168/2).moveTo(-15,52).cylinder(168,48))