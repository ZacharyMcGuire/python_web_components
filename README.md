# Python Web Components

A pythonic approach to rendering HTML.

## But why?

Conceptually, I quite like React & Vue. But, with my career being in Data & Analytics my skills are in SQL & Python.
Sure, I could pick up JS/TS if I really wanted to, but Python already has some excellent web frameworks like Django, FastAPI & Litestar (to name a few).
The reality is also that none of the projects I've ever thought of throwing a UI over actually have a need to be React (or Vue, Angular, Flutter, etc). I'd bet the majority of internal apps probably don't.

In my experience, the only major thing that's lacking from these Python frameworks is a reliable & DRY way of rendering HTML components.

Templating languages like Jinja2 are awesome libraries, and I certainly recommend their use - they're a part of my daily life thanks to tools like dbt.

However, I find them to fall short in two key areas:
1. Support for Type Hinting.
2. DRY HTML / Templates.

Jinja2 for example, has things like includes, extends, macros, etc but it's easy to start to lose track of interdependencies without these having physical linkage to the rest of the Python app, or even within the Templates.
Then there's params, "context" and - to steal some React terminology, props.
The approach taken by these templating libraries feels a little too ✨ magic ✨ for anything beyond the basics.

Classes strike me as one way of addressing this: 
1. Define a data structure for your component's props (if any).
2. Define your component as a Class, rendering child components as needed.

This gives us all the beautiful functionality of being an Object, like type hinting, and the ability to use dataclasses (or even Pydantic models!) as constructors for props. Similar to React, we can also pass these classes as children of other classes to build out our HTML Document, giving us DRY HTML.

With the addition of a library like HTMX we're also able to selectively reload or swap out sections of our page, among other cool things, getting us pretty close to what might be the perfect python web ecosystem.

## Where to from here?

I'm only a few hours into building out the initial concepts. If you stumble across this project, feel free to browse but I wouldn't suggest using it.
I doubt I'm the first person to think of this approach, which means there's likely to be a good reason we use templating libraries and not classes - I probably just haven't realised it yet.

I also have no idea how much time I'll actually commit to this idea or how well it'll turn out.
