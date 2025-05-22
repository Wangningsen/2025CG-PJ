import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,17,0))
r=w0.sketch().push([(-95,-42)]).circle(5).push([(39.5,-6)]).rect(121,136).finalize().extrude(-106).union(w0.sketch().push([(6,35)]).circle(39).circle(18,mode='s').finalize().extrude(72))