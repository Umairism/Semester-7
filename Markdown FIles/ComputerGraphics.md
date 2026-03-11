# Computer Graphics – Course Notes

## Table of Contents

- [Introduction to Computer Graphics & HCI](#introduction-to-computer-graphics--hci)
- [Types of Graphics](#types-of-graphics)
- [Image Processing vs Computer Graphics vs Pattern Recognition](#image-processing-vs-computer-graphics-vs-pattern-recognition)
- [Applications of Computer Graphics](#applications-of-computer-graphics)
- [Lecture 3: Elements of Computer-Generated Pictures](#lecture-3-elements-of-computer-generated-pictures)
- [Graphics Display Devices](#graphics-display-devices)
- [Graphics Pipeline](#graphics-pipeline)
- [Jakob Nielsen's 10 Usability Heuristics](#jakob-nielsens-10-usability-heuristics)
- [Process of Interactive Design](#process-of-interactive-design)
- [Activity 1: Yahoo! India Webpage — Heuristic Evaluation](#activity-1-yahoo-india-webpage--heuristic-evaluation)
- [Transformations](#transformations)
- [Compilation Commands](#compilation-commands)

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

## Jakob Nielsen's 10 Usability Heuristics

These are fundamental principles for designing user-friendly interfaces:

| # | Heuristic | Description |
|:-:|:--|:--|
| 1 | **Visibility of System Status** | The system should keep users informed about what is going on through timely feedback |
| 2 | **Match Between System & Real World** | Use language, concepts, and conventions familiar to the user |
| 3 | **User Control & Freedom** | Provide undo, redo, and easy navigation so users can recover from mistakes |
| 4 | **Consistency & Standards** | Follow platform and industry conventions — don't make users wonder if different words/actions mean the same thing |
| 5 | **Error Prevention** | Design to prevent errors from occurring in the first place |
| 6 | **Recognition Over Recall** | Minimize memory load by making elements, actions, and options visible |
| 7 | **Flexibility & Efficiency of Use** | Provide shortcuts and accelerators for experienced users |
| 8 | **Aesthetic & Minimalist Design** | Avoid irrelevant or rarely needed information — every extra element competes for attention |
| 9 | **Help Users Recognize, Diagnose & Recover from Errors** | Error messages should be in plain language, indicate the problem, and suggest a solution |
| 10 | **Help & Documentation** | Provide searchable help focused on the user's task |

---

## Process of Interactive Design

### Paper Prototyping & Digital Wireframing

| Method | Fidelity | Description |
|:--|:--|:--|
| **Paper Prototyping** | Low Fidelity | Hand-drawn sketches of interfaces for early-stage feedback — fast, cheap, disposable |
| **Digital Wireframing** | Medium–High Fidelity | Digital layouts created with tools (e.g., Figma, Balsamiq) showing structure and interaction flow |

> Paper prototypes are ideal for brainstorming and early validation, while digital wireframes are used for more detailed design iterations.

---

## Activity 1: Yahoo! India Webpage — Heuristic Evaluation

| Heuristic | Yes/No | Justification |
|:--|:--|:--|
| **Visibility** | No | No organized set of elements — the site rushes a bunch of elements at the user |
| **Match System & Real World** | Yes | Logos and pictorial elements closely relate to real-world depictions |
| **User Control** | Yes | Back buttons, undo options, and navigation links allow free navigation |
| **Consistency** | No | Inconsistent font sizes, colors, and layout across different sections |
| **Error Prevention** | No | Search bar lacks auto-suggestions or confirmation prompts |
| **Recognition Over Recall** | Yes | Navigation menus, icons, and categories are visible, reducing need to memorize paths |
| **Flexibility** | No | Limited shortcuts or personalization options for experienced users |
| **Minimalist Design** | No | Page is heavily cluttered with ads, links, and content competing for attention |
| **Help Recover from Errors** | No | No clear error messages or guided recovery (e.g., for broken links) |

---

## Activity 2: HTML & CSS Login Page

A fully minimalist login page was created as a lab task demonstrating the **Minimalist Design** heuristic.

> File location: `Computer Graphics/Lab_Task/Tasks/login.html`

---

## Transformations

Transformations are operations that modify the position, size, or orientation of objects in space.

### Types

| Category | Description |
|:--|:--|
| **Solid Body Transformations** | Preserve shape and size (rigid body) |
| **Affine Transformations** | Preserve parallelism — includes translation, scaling, rotation, reflection, and shearing |

### Affine Transformations

| Transformation | Effect |
|:--|:--|
| **Translation** | Move an object from one position to another |
| **Scaling** | Resize an object (enlarge or shrink) |
| **Rotation** | Turn an object around a fixed point |
| **Reflection** | Mirror an object across an axis |
| **Shearing** | Slant/skew an object along an axis |

---

### Translation

Moves an object by a displacement vector $(t_x, t_y)$ in 2D or $(t_x, t_y, t_z)$ in 3D.

**2D Formula:**

$$(x', y') = (x + t_x, \; y + t_y)$$

**3D Formula:**

$$(x', y', z') = (x + t_x, \; y + t_y, \; z + t_z)$$

**2D Translation Matrix (Homogeneous Coordinates):**

$$
T = \begin{bmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{bmatrix}
$$

**3D Translation Matrix (Homogeneous Coordinates):**

$$
T = \begin{bmatrix} 1 & 0 & 0 & t_x \\ 0 & 1 & 0 & t_y \\ 0 & 0 & 1 & t_z \\ 0 & 0 & 0 & 1 \end{bmatrix}
$$

---

### Scaling

Resizes an object by scaling factors $s_x$ and $s_y$:

$$(x', y') = (s_x \cdot x, \; s_y \cdot y)$$

**2D Scaling Matrix:**

$$
S = \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

> - $s > 1$: Enlarges the object
> - $0 < s < 1$: Shrinks the object
> - $s = 1$: No change

---

## Compilation Commands

Commands used to compile OpenGL C++ programs:

```bash
# Single file
g++ -fdiagnostics-color=always -g Main.cpp -o Main -lGL -lGLU -lglut

# Multiple files (e.g., House project)
g++ -fdiagnostics-color=always -g main.cpp triangle.cpp circle.cpp square.cpp line.cpp rectangle.cpp -o House -lGL -lGLU -lglut
```

> The `-lGL -lGLU -lglut` flags link the OpenGL, GLU, and GLUT libraries respectively.

---

*These notes cover Computer Graphics topics from Semester 7 — fundamentals of CG & HCI, display devices (CRT, raster), graphical elements, the GPU pipeline, image formation, usability heuristics, interactive design, transformations (translation, scaling), and compilation commands.*
