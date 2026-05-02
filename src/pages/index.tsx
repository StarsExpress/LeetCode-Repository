import React, {useState} from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import problems from '../data/problems.json';

const ITEMS_PER_PAGE = 12;

// Use Record<string, string> to prevent error marks in PyCharm.
const difficultyColor: Record<string, string> = {
  Easy: '#00b8a3',
  Medium: '#ffc01e',
  Hard: '#ff375f',
};

export default function Home() {
  const [page, setPage] = useState(1);
  const totalPages = Math.ceil(problems.length / ITEMS_PER_PAGE);
  const current = problems.slice((page - 1) * ITEMS_PER_PAGE, page * ITEMS_PER_PAGE);

  return (
    <Layout title="天碼行空 SkyHorse" description="LeetCode 題解">
      <main style={{maxWidth: 1200, margin: '0 auto', padding: '2rem 1rem'}}>

        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(3, 1fr)', // 3 per row.
          gap: '1.5rem',
        }}>
          {current.map((p) => (
            <Link
              key={p.number}
              to={`/docs/${p.docId}`}
              style={{textDecoration: 'none'}}>
              <div style={{
                borderRadius: 12,
                overflow: 'hidden',
                border: '1px solid var(--ifm-color-emphasis-200)',
                transition: 'transform 0.2s',
                cursor: 'pointer',
              }}
              onMouseEnter={e => (e.currentTarget.style.transform = 'translateY(-4px)')}
              onMouseLeave={e => (e.currentTarget.style.transform = 'translateY(0)')}>

                {p.img && (
                  <img
                    src={p.img}
                    alt={p.title}
                    style={{width: '100%', height: 160, objectFit: 'cover'}}
                  />
                )}

                <div style={{padding: '0.75rem 1rem'}}>
                  <div style={{fontWeight: 600, marginBottom: 6}}>{p.title}</div>
                  <div style={{display: 'flex', gap: 8, fontSize: 12}}>
                    <span style={{
                      background: 'var(--ifm-color-emphasis-100)',
                      borderRadius: 4,
                      padding: '2px 8px',
                    }}>{p.topic}</span>
                    <span style={{
                      background: difficultyColor[p.difficulty] + '22',
                      color: difficultyColor[p.difficulty],
                      borderRadius: 4,
                      padding: '2px 8px',
                      fontWeight: 600,
                    }}>{p.difficulty}</span>
                  </div>
                </div>
              </div>
            </Link>
          ))}
        </div>

        {/* 分頁 */}
        <div style={{display: 'flex', justifyContent: 'center', gap: 8, marginTop: '2rem'}}>
          {Array.from({length: totalPages}, (_, i) => i + 1).map(n => (
            <button
              key={n}
              onClick={() => setPage(n)}
              style={{
                width: 36, height: 36,
                borderRadius: 8,
                border: '1px solid var(--ifm-color-emphasis-300)',
                background: n === page ? 'var(--ifm-color-primary)' : 'transparent',
                color: n === page ? 'white' : 'inherit',
                cursor: 'pointer',
                fontWeight: n === page ? 600 : 400,
              }}>
              {n}
            </button>
          ))}
        </div>

      </main>
    </Layout>
  );
}