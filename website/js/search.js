document.addEventListener(
"input",
(event)=>{

    if(
        event.target.id !==
        "searchInput"
    ){
        return;
    }

    const query =
    event.target.value
    .toLowerCase();

    const filtered =
    ALL_POSTS.filter(post=>{

        return (

            post.title
            .toLowerCase()
            .includes(query)

            ||

            post.description
            .toLowerCase()
            .includes(query)

        );

    });

    renderPosts(filtered);

});