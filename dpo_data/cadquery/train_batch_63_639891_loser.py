import cadquery as cq
w0=cq.Workplane('YZ',origin=(47,0,0))
r=w0.sketch().push([(-44.5,3.5)]).rect(43,23).push([(-35,6)]).circle(2,mode='s').push([(-44.5,88.5)]).rect(43,23).push([(27,-61)]).circle(39).finalize().extrude(-93)