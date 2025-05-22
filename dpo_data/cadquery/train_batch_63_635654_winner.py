import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,5))
r=w0.sketch().arc((-24,-77),(96,-29),(23,74)).arc((-96,33),(-24,-77)).assemble().push([(-20,9)]).circle(20,mode='s').push([(5.5,57.5)]).rect(11,13,mode='s').finalize().extrude(-9)