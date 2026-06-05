let ALL_POSTS = [];

async function loadPosts(){

    const response =
    await fetch(
        "data/posts.json"
    );

    const posts =
    await response.json();

    ALL_POSTS = posts;

    renderPosts(posts);
}

function renderPosts(posts){

    const container =
    document.getElementById(
        "postsContainer"
    );

    container.innerHTML = "";

    posts.forEach(post=>{

        const card =
        document.createElement(
            "div"
        );

        card.className =
        "post-card";

        const keywords =
        post.keywords
        ?
        post.keywords.split(",")
        :
        [];

        const tags =
        keywords
        .slice(0,4)
        .map(tag=>
        `
        <span class="tag">
            ${tag.trim()}
        </span>
        `
        )
        .join("");

        card.innerHTML =

        `
        <h2 class="post-title">
            ${post.title}
        </h2>

        <p class="post-desc">
            ${post.description}
        </p>

        <div class="meta">

            <span>
                ${post.source}
            </span>

            <span>
                ${post.author}
            </span>

        </div>

        <div class="tags">
            ${tags}
        </div>
        `;

        container.appendChild(
            card
        );
    });
}

loadPosts();