import Index from '../pages/Index.svelte';

const app = new Index({
    target: document.getElementById("index-target"),
    props: JSON.parse(document.getElementById("index-props").textContent),
});

export default app;
