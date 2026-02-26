# Computer Graphics – Course Notes

## Table of Contents

- [Introduction to Computer Graphics & HCI](#introduction-to-computer-graphics--hci)
- [Types of Graphics](#types-of-graphics)
- [Image Processing vs Computer Graphics vs Pattern Recognition](#image-processing-vs-computer-graphics-vs-pattern-recognition)
- [Applications of Computer Graphics](#applications-of-computer-graphics)
- [Lecture 3: Elements of Computer-Generated Pictures](#lecture-3-elements-of-computer-generated-pictures)
- [Graphics Display Devices](#graphics-display-devices)
- [Graphics Pipeline](#graphics-pipeline)

---

## Introduction to Computer Graphics & HCI

**Computer Graphics** is the field concerned with the creation the of visual content (objects, images, animations) from scratch using computational methods. **HCI (Human-Computer Interaction)** studies how users interact with these graphical systems.

### Frame Buffer

A **Frame Buffer** is a temporary memory location used to prevent delays while processing and displaying images. It acts as a synchronous buffer between computation and display — the image is fully composed in the buffer before being sent to the screen.

> **Key Idea:** The frame buffer ensures smooth, flicker-free rendering by decoupling image generation from display output.

---

## Types of Graphics

### 2D Graphics
- **Transformations:** Changes in size, position, and angle of objects on a 2D plane.

### 3D Graphics
- Works with **X, Y, and Z axes** along with additional properties like **lighting**, **shading**, and **perspective**.

### Other Areas

| Area | Description |
|:--|:--|
| **Rendering** | Converting 3D models into 2D images with color, lighting, and shadows |
| **Animation** | Creating the illusion of motion through sequences of frames |
| **Visualization** | Graphical representation of data and information |
| **CAD (Computer Aided Design)** | Using software to create precision drawings and technical illustrations |

---

## Image Processing vs Computer Graphics vs Pattern Recognition

These three fields are related but distinct:

| Field | Focus |
|:--|:--|
| **Image Processing** | Advancements, editing, enhancements, and alteration of *existing* images |
| **Computer Graphics** | Creation of images and visual content *from scratch* |
| **Pattern Recognition** | Identifying patterns and regularities in data (e.g., images, signals) |

---

## Applications of Computer Graphics

### Usage of Computer-Designed Pictures

- Arts, entertainment, and publishing
- Movie production, animation, and special effects
- Computer games
- Web browsers on the WWW
- Paint systems and digital art tools
- Process monitoring and control
- Displaying simulations
- Computer-aided design (CAD)

### Broader Applications

| Application | Examples |
|:--|:--|
| **GUI** | Menus, icons, cursors, dialog boxes |
| **Scientific Visualization** | Presentation graphics, data plots |
| **Entertainment** | Games, movies, VR experiences |
| **Architecture** | 3D architectural scenes and walkthroughs |
| **Medicine** | Medical imaging (MRI, CT scans, 3D organ models) |
| **Virtual Worlds** | Simulated environments and VR |
| **Education** | Interactive learning tools and simulations |

---

## Lecture 3: Elements of Computer-Generated Pictures

### Core Elements

| Element | Description |
|:--|:--|
| **Pixels** | The smallest addressable unit on a display |
| **Color** | RGB values defining hue, saturation, and brightness |
| **Shapes & Objects** | Geometric primitives (lines, circles, polygons) |
| **Textures** | Surface detail mapped onto objects |
| **Lighting** | Simulated light sources affecting appearance |
| **Rendering Techniques** | Methods to convert models to images (ray tracing, rasterization) |
| **Composition** | Arrangement and layering of visual elements |
| **Effects** | Post-processing like blur, bloom, anti-aliasing |

### Graphical Primitives

| Primitive | Description |
|:--|:--|
| **Polyline** | A connected sequence of multiple line segments |
| **Text** | Character rendering on screen |
| **Filled Region** | A closed area filled with color or pattern |

### Raster Images vs Vector Graphics

| Raster | Vector |
|:--|:--|
| Made of pixels (bitmap) | Made of mathematical paths |
| Resolution-dependent | Resolution-independent (scalable) |
| Used for photos, textures | Used for logos, illustrations, CAD |

### Types of Graphics Systems

| Type | Description |
|:--|:--|
| **Active** | Systems that refresh/redraw the display continuously |
| **Passive** | Systems that display a static image without refresh |

### CSG (Constructive Solid Geometry)

A technique for creating complex 3D shapes by **combining simpler geometric primitives** using Boolean operations (union, intersection, difference).

---

## Graphics Display Devices

### Vector Display

Vector displays draw images by directing an electron beam to trace out lines and shapes directly.

#### CRT (Cathode Ray Tube) — Oscilloscope-Based

- **Phosphors** — Materials that glow when hit by an electron beam
  - **Fluorescence** — Light emitted *during* electron bombardment
  - **Phosphorescence** — Light emitted *after* bombardment ceases
  - **Persistence** — How long the phosphor continues to glow
    - **Long Persistence** — Glows longer, less flicker, but causes ghosting
    - **Short Persistence** — Fades quickly, requires frequent refresh

#### CRT-Based Display Types

| Display Type | Description |
|:--|:--|
| **DVST** (Direct View Storage Tube) | Retains image without refresh; no flicker but cannot selectively erase |
| **Calligraphic / Random Scan** | Draws lines in any order; good for wireframe models |
| **Raster Scan** | Draws pixels row by row in a fixed pattern |

---

### Raster Display

Raster displays represent images as a **grid of pixels** scanned in a fixed pattern.

#### Key Concepts

| Concept | Description |
|:--|:--|
| **Raster** | A grid/matrix of pixels |
| **Pixel** | A single point in the raster grid |
| **Scan Pattern** | Left to right, top to bottom (like reading English) |
| **Frame Buffer** | Memory that stores the pixel values for the entire screen |
| **Graphics Card** | Hardware that manages the frame buffer and drives the display |

#### LUT (Look-Up Table) Memory

The **Look-Up Table** maps stored pixel values to actual display colors:

- **Total colors available:** $2^w$ (where $w$ = width of LUT entries)
- **Colors displayable at one time:** $2^b$ (where $b$ = bits per pixel in the frame buffer)

> The **frame buffer size** and **LUT memory** together determine the color depth and resolution of the display.

#### Active Matrix Display

A modern flat-panel technology (e.g., LCD, OLED) where each pixel is controlled by one or more **thin-film transistors (TFTs)**, enabling precise control and fast refresh rates.

---

## Graphics Pipeline

The **graphics pipeline** is the sequence of stages that transforms 3D scene data into a 2D image on screen. It is split between the **CPU** and **GPU**:

### Pipeline Stages

```
┌──────────────────┐
│   APPLICATION    │  ← CPU
│   COMMANDS       │  ← CPU
├──────────────────┤
│   GEOMETRY       │  ← GPU
│   RASTERIZATION  │  ← GPU
│   FRAGMENT       │  ← GPU
│   DISPLAY        │  ← GPU
└──────────────────┘
```

| Stage | Processor | Description |
|:--|:--|:--|
| **Application** | CPU | Scene management, user input, physics |
| **Commands** | CPU | API calls sent to the GPU |
| **Geometry** | GPU | Vertex transformations, projections |
| **Rasterization** | GPU | Converting geometry to pixel fragments |
| **Fragment** | GPU | Computing final color for each pixel |
| **Display** | GPU | Outputting the final image to screen |

### Image Formation Steps

| Step | Operation | Description |
|:--|:--|:--|
| 1. **Vertex Processing** | Transformation | Transform vertices from model space to screen space |
| 2. **Clipping & Rasterization** | Convert to Pixels | Clip geometry to the viewport and convert to pixel fragments |
| 3. **Fragment Processing** | Compute Final Colors | Apply textures, lighting, and shading per fragment |
| 4. **Frame Buffer Processing** | Blending & Hidden-Surface Removal | Combine fragments, resolve depth (Z-buffer), and produce final image |

---

*These notes cover Computer Graphics topics from Semester 7 — fundamentals of CG & HCI, display devices (CRT, raster), graphical elements, the GPU pipeline, and image formation.*
