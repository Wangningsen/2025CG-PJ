import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,89,0))
r=w0.sketch().push([(-6,80)]).circle(20).push([(12,-87)]).circle(13).push([(17,-82)]).rect(4,4,mode='s').finalize().extrude(-178)