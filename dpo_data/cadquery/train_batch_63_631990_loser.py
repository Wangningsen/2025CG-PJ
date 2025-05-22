import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-79))
r=w0.sketch().rect(98,200).push([(-17.5,-77)]).rect(29,36,mode='s').push([(46,59)]).circle(3,mode='s').finalize().extrude(158)