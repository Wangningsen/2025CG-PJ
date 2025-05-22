import cadquery as cq
w0=cq.Workplane('YZ',origin=(34,0,0))
r=w0.sketch().push([(47,-40.5)]).rect(14,119).push([(47,-41)]).circle(3,mode='s').push([(47,-1)]).circle(3,mode='s').finalize().extrude(-68).union(w0.sketch().push([(-40,86)]).circle(14).circle(13,mode='s').finalize().extrude(-27))