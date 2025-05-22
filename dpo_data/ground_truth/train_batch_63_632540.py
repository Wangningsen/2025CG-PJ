import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().arc((-38,-28),(-33,-28),(-33,-33)).arc((-24,-40),(-14,-45)).segment((-14,-82)).segment((14,-82)).segment((14,-45)).arc((47,0),(14,45)).segment((14,82)).segment((-14,82)).segment((-14,45)).arc((-45,14),(-38,-28)).assemble().circle(40,mode='s').finalize().extrude(200)