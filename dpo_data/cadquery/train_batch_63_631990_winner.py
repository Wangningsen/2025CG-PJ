import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-78))
r=w0.sketch().rect(98,200).push([(-17.5,-77)]).rect(29,36,mode='s').push([(45,58)]).circle(2,mode='s').finalize().extrude(157)