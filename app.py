from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/~/bolt-astro-blog')
def bolt_astro_blog():
    return "Start a blog with Astro"

@app.route('/~/bolt-vitepress')
def bolt_vitepress():
    return "Create a docs site with Vitepress"

@app.route('/~/bolt-shadcn')
def bolt_shadcn():
    return "Scaffold UI with shadcn"

@app.route('/~/bolt-slidev')
def bolt_slidev():
    return "Draft a presentation with Slidev"

@app.route('/~/bolt-astro-basic')
def bolt_astro_basic():
    return "Start a blank app with Astro"

@app.route('/~/bolt-vanilla-vite')
def bolt_vanilla_vite():
    return "Start a blank app with Vanilla Vite"

@app.route('/~/bolt-nextjs-shadcn')
def bolt_nextjs_shadcn():
    return "Start a blank app with Next.js and Shadcn"

@app.route('/~/bolt-nativescript-js')
def bolt_nativescript_js():
    return "Start a blank app with NativeScript JS"

@app.route('/~/bolt-nuxt')
def bolt_nuxt():
    return "Start a blank app with Nuxt"

@app.route('/~/bolt-slidev')
def bolt_slidev_blank():
    return "Start a blank app with Slidev"

@app.route('/~/bolt-vue')
def bolt_vue():
    return "Start a blank app with Vue"

@app.route('/~/bolt-sveltekit')
def bolt_sveltekit():
    return "Start a blank app with SvelteKit"

@app.route('/~/bolt-remix')
def bolt_remix():
    return "Start a blank app with Remix"

@app.route('/~/bolt-ts')
def bolt_ts():
    return "Start a blank app with TypeScript"

@app.route('/~/bolt-vite-react')
def bolt_vite_react():
    return "Start a blank app with Vite and React"

@app.route('/~/bolt-remotion')
def bolt_remotion():
    return "Start a blank app with Remotion"

@app.route('/~/bolt-angular')
def bolt_angular():
    return "Start a blank app with Angular"

@app.route('/~/bolt-qwik')
def bolt_qwik():
    return "Start a blank app with Qwik"

if __name__ == '__main__':
    app.run(debug=True)
