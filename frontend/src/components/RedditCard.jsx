import React from "react"

const RedditCard = ({results }) => {
    if (!results) {
        return null;
    }

    return (
        <div className="reddit-card">
            <h2>Top Reddit Posts</h2>
            {results.reddit_error ? (
                <div className="error-message">
                    <p>Error fetching Reddit posts: {results.reddit_error}</p>
                </div>
            ) : (
                results.reddit_results.map((post, index) =>(
                <div key={index} className="reddit-post">
                    <h4>{post.title}</h4>
                    <p>{post.snippet}</p>
                    <p>{post.displayed_link}</p>
                    <a href={post.link} target="_blank" rel="noopener noreferrer">View Post</a>
                </div>
            ))
            )}
            
        </div>
    )
}
export default RedditCard;