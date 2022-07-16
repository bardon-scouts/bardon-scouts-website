import React from "react";
import PropTypes from "prop-types";
import { graphql } from "gatsby";
import Layout from "../components/Layout";
import Content, { HTMLContent } from "../components/Content";

// eslint-disable-next-line
export const ThanksTemplate = ({ title, content, contentComponent }) => {
  const PageContent = contentComponent || Content;

  return (

    <section className="section">
      <div className="container">
        <div className="content">
          <h1>{title}</h1>
          <PageContent className="content" content={content} />
        </div>
        <p><a href="/">&lt; Back</a></p>
      </div>
    </section>


  );
};

ThanksTemplate.propTypes = {
  title: PropTypes.string.isRequired,
  content: PropTypes.string,
  contentComponent: PropTypes.func,
};

const Thanks = ({ data }) => {
  const { markdownRemark: post } = data;

  return (
    <Layout>
      <ThanksTemplate
        contentComponent={HTMLContent}
        title={post.frontmatter.title}
        content={post.html}
      />
    </Layout>
  );
};

Thanks.propTypes = {
  data: PropTypes.object.isRequired,
};

export default Thanks;

export const thanksQuery = graphql`
  query Thanks($id: String!) {
    markdownRemark(id: { eq: $id }) {
      html
      frontmatter {
        title
        image {
          childImageSharp {
            gatsbyImageData(quality: 100, layout: FULL_WIDTH)
          }
        }
      }
    }
  }
`;
