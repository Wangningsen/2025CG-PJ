import cadquery as cq
w0=cq.Workplane('YZ',origin=(17,0,0))
r=w0.sketch().push([(35,-34.5)]).rect(130,69).push([(-24,-22)]).rect(6,6,mode='s').finalize().extrude(-101).union(w0.sketch().push([(-74,43)]).circle(26).circle(18,mode='s').finalize().extrude(67))